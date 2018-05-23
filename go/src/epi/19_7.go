package main

import (
	"bufio"
	"container/heap"
	"log"
	"os"
	"sync"
	"time"
)

// Task represents a scheduled cancellable function.
type Task struct {
	start     time.Time
	index     int
	fn        func()
	cancelled bool
}

// Cancel prevents a Task from being run, if it hasn't run yet.
func (t *Task) Cancel() {
	t.cancelled = true
}

// A min-heap of tasks, ordered by start time.
type tasks []*Task

func (ts tasks) Len() int {
	return len(ts)
}

func (ts tasks) Less(i, j int) bool {
	return ts[i].start.Before(ts[j].start)
}

func (ts tasks) Swap(i, j int) {
	ts[i], ts[j] = ts[j], ts[i]
	ts[i].index = i
	ts[j].index = j
}

func (ts *tasks) Push(t interface{}) {
	task := t.(*Task)
	n := len(*ts)
	task.index = n
	*ts = append(*ts, task)
}

func (ts *tasks) Pop() interface{} {
	old := *ts
	n := len(*ts)
	t := old[n-1]
	t.index = -1 // for safety
	*ts = old[0 : n-1]
	return t
}

var (
	mu sync.Mutex
	ts tasks
	ch chan bool
)

func init() {
	ch = make(chan bool, 10)
	ts = make([]*Task, 0)
	heap.Init(&ts)
}

func schedule(fn func(), start time.Time) *Task {
	t := &Task{start: start, fn: fn}

	log.Printf("scheduling task %v\n", *t)

	mu.Lock()
	heap.Push(&ts, t)
	go func() {
		// note: potential goroutine leak
		ch <- true
	}()
	mu.Unlock()

	log.Printf("scheduled task %v\n", *t)

	return t
}

func dispatcher() {
	for {
		// default timeout of 1 day so the loop isn't busy
		timeout := time.Duration(24 * time.Hour)

		mu.Lock()
		for len(ts) != 0 && ts[0].cancelled {
			heap.Pop(&ts)
		}
		if len(ts) != 0 {
			task := ts[0]
			timeout = task.start.Sub(time.Now())
		}
		mu.Unlock()

		select {
		case <-time.After(timeout):
			mu.Lock()
			task := heap.Pop(&ts).(*Task)
			mu.Unlock()
			go task.fn()
		case <-ch:
		}
	}
}

func main() {
	var wg sync.WaitGroup

	start := time.Now()

	task := func(j int) func() {
		return func() {
			log.Printf("running %d: %v \n", j, time.Since(start))
		}
	}

	wg.Add(1)
	go func() {
		log.Println("Press ENTER to quit.")
		r := bufio.NewReader(os.Stdin)
		r.ReadRune()
		close(ch)
		log.Print("Goodbye!")
		wg.Done()
	}()
	go dispatcher()
	go func() {
		schedule(task(1), start.Add(1*time.Second))
		t := schedule(task(2), start.Add(2*time.Second))
		t.Cancel()
		schedule(task(3), start.Add(3*time.Second))
		schedule(task(4), start.Add(2500*time.Millisecond))

		time.Sleep(5 * time.Second)
		newStart := time.Now()
		schedule(task(5), newStart.Add(5*time.Second))
		schedule(task(6), newStart.Add(4*time.Second))
		schedule(task(7), newStart.Add(3500*time.Millisecond))
	}()

	wg.Wait()
}

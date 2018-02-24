 (define (fib n)
  (cond
   ((= n 0) 0)
   ((= n 1) 1)
   (else (+ (fib (- n 1)) (fib (- n 2))))
  )
 )
 
 (define (fib n)
  (define (fib-calc n x y)
   (if (= n 0)
    y
    (fib-calc (- n 1) y (+ x y))
   )
  )
  (fib-calc n 1 0)
 )

 (define (reverse lst)
  (define (reverse-calc lst des)
   (
    if (null? lst)
     des
    (reverse-calc (cdr lst) (cons (car lst) des))
   )
  )
  (reverse-calc lst nil)
 )
(define (find s predicate)
 (cond
  ((null? s) false)
  ((predicate (car s)) (car s))
  (else (find (cdr-stream s) predicate))
 )
)

(define (scale-stream s k)
 (cond
  ((null? s) nil)
  (else (cons-stream (* (car s) k) (scale-stream (cdr-stream s) k)))
 )
)

(define (has-cycle s)
 (define (cycle s t)
  (cond
   ((null? t) false)
   ((eq? s t) true)
   (else (cycle s (cdr-stream t)))
  )
 )
 (cycle s (cdr-stream s))
)
(define (has-cycle-constant s)
  'YOUR-CODE-HERE
)

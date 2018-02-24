(define (factorial x)
    (cond
        ((= x 0) 1)
        (else (* x (factorial (- x 1))))
    )
)

(define (fib n)
  (if (< n 2) 1
   (+ (fib (- n 1)) (fib (- n 2)))
  )
)

(define (concat a b)
 (if (null? a) b
   (cons (car a) (concat (cdr a) b))
 )
)

(define (replicate x n)
 (if (= n 0) nil
  (cons x (replicate x (- n 1)))
 )
)

(define (uncompress s)
 (if (null? s) nil
  (concat (replicate (car (car s)) (car (cdr (car s)))) (uncompress (cdr s)))
 )
)

(define (map fn lst)
(if (null? lst)
nil
(cons (fn (car lst)) (map fn (cdr lst)))))

(define (deep-apply fn nested-list)
    (cond
     ((null? nested-list) nil)
     ((integer? nested-list) fn nested-list)
     ((list? (car nested-list)) (cons (deep-apply fn (car nested-list)) (deep-apply fn (cdr nested-list))))
     (else (cons (fn (car nested-list)) (deep-apply fn (cdr nested-list))))
    )
)


(define (map-stream f s)
 (cond
  ((null? s) nil)
  (else (cons-stream (f (car s)) (map-stream f (cdr-stream s))))
 )
)

(define (range-stream start end)
 (cond
  ((= start end) nil)
  (else (cons-stream start (range-stream (+ 1 start) end)))
 )
)

(define (slice stream start end)
 (cond
  ((null? stream) nil)
  ((and (>= (car stream) start) (< (car stream) end)) (cons-stream (car stream) (slice (cdr-stream stream) start end)))
  (else (slice (cdr-stream stream) start end))
 )
)
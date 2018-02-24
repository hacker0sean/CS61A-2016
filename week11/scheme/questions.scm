(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))


(define (map proc items)
 (cond
  ((null? items) nil)
  (else (cons (proc (car items)) (map proc (cdr items))))
 )
)

(define (cons-all first rests)
 (cond
  ((null? rests) nil)
  (else (cons (cons first (car rests)) (cons-all first (cdr rests))))
 )
)

(define (zip pairs)
 (cond
  ((null? pairs) (cons nil (cons nil nil)))
  (else
   (define s (zip (cdr pairs)))
   (cons (cons (car (car pairs)) (car s)) (cons (cons (car (cdr (car pairs))) (cadr s)) nil))
  )
 )
)


(define (enumerate s)
 (define (enum s a)
  (
   cond
   ((null? s) nil)
   (else (cons (cons a (cons (car s ) nil)) (enum (cdr s) (+ a 1))))
  )
 )
 (enum s 0)
)

(define (list-change total denoms)
 (cond
  ((= total 0) (cons nil nil))
  ((or (< total 0) (< (length denoms) 1)) nil)
  (else (append (cons-all (car denoms) (list-change (- total (car denoms)) denoms)) (list-change total (cdr denoms))))
 )
)

(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))


(define (let-to-lambda expr)
  (cond ((atom? expr)
         expr
         )
        ((quoted? expr)
         expr
         )
   ((or (lambda? expr)
     (define? expr))
    (let ((form (car expr))
          (params (cadr expr))
          (body (cddr expr)))
     
     (append (list form params) (map let-to-lambda body))
    )
   )
   ((let? expr)
    (let ((values (cadr expr))
          (body (cddr expr)))
     (append (list (append (list 'lambda (car (zip values))) (map let-to-lambda body))) (map let-to-lambda (cadr (zip values))))
    )
   )
   (else
     (map let-to-lambda expr)
   ))
  )
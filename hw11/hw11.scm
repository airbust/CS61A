(define (find s predicate)
  'YOUR-CODE-HERE
  (if (null? s)
      #f
      (if (predicate (car s))
          (car s)
          (find (cdr-stream s) predicate)))
)

(define (scale-stream s k)
  'YOUR-CODE-HERE
  (if (null? s)
      nil
      (cons-stream (* k (car s)) (scale-stream (cdr-stream s) k)))
)

(define (has-cycle s)
  'YOUR-CODE-HERE
  (define (helper fast slow)
    (cond ((or (null? fast) (null? (cdr-stream fast))) #f)
          ((eq? fast slow) #t)
          (else (helper (cdr-stream (cdr-stream fast)) (cdr-stream slow)))))
  (helper (cdr-stream s) s)
)
(define (has-cycle-constant s)
  'YOUR-CODE-HERE
  (define (helper fast slow)
    (cond ((or (null? fast) (null? (cdr-stream fast))) #f)
          ((eq? fast slow) #t)
          (else (helper (cdr-stream (cdr-stream fast)) (cdr-stream slow)))))
  (helper (cdr-stream s) s)
)

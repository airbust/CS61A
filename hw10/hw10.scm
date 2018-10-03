(define (accumulate combiner start n term)
  (if (= n 0)
      start
      (combiner (term n) (accumulate combiner start (- n 1) term))
  )
)

(define (accumulate-tail combiner start n term)
  'YOUR-CODE-HERE
  (define (helper n res)
    (if (= n 0)
        res
        (helper (- n 1) (combiner (term n) res))))
  (helper n start)
)

(define-macro (list-of expr for var in seq if filter-fn)
  'YOUR-CODE-HERE
  `(map (lambda (,var) ,expr) (filter (lambda (,var) ,filter-fn) ,seq))
)

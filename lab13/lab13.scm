; Q1
(define (compose-all funcs)
  'YOUR-CODE-HERE
  (if (null? funcs)
      (lambda (x) x)
      (lambda (x) ((compose-all (cdr funcs)) ((car funcs) x))))
)

; Q2
(define (tail-replicate x n)
  'YOUR-CODE-HERE
  (define (tail-replicate-iter k re)
    (if (= k n)
        re
        (tail-replicate-iter (+ k 1) (cons x re))))
  (tail-replicate-iter 0 nil)
)

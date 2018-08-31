; Q4
(define (rle s)
  'YOUR-CODE-HERE
  (define (append s x)
    (if (null? s)
        (cons x nil)
        (cons (car s) (append (cdr-stream s) x))))
  (define lst nil)
  (define (count s x cnt)
    (if (null? s)
        nil
        (if (eq? (car s) x)
            (count (cdr-stream s) x (+ 1 cnt))
            (append lst (count (cdr-stream s) (car s) 1)))))

  (cond ((null? s) nil)
        ((null? (cdr s)) )
        (else (if (eq? (car (cdr s)) (car s))
                  (count (cdr s) (+ cnt 1) lst)
                  (cons lst (cons (car s) (cons cnt nil))))))
)

; Q4 testing functions
(define (list-to-stream lst)
    (if (null? lst) nil
                    (cons-stream (car lst) (list-to-stream (cdr lst))))
)

(define (stream-to-list s)
    (if (null? s) nil
                 (cons (car s) (stream-to-list (cdr-stream s))))
)

; Q5
(define (insert n s)
  'YOUR-CODE-HERE
)

; Q6
(define (deep-map fn s)
  'YOUR-CODE-HERE
  nil
)

; Q7
; Feel free to use these helper procedures in your solution
(define (map fn s)
  (if (null? s) nil
      (cons (fn (car s))
            (map fn (cdr s)))))

(define (filter fn s)
  (cond ((null? s) nil)
        ((fn (car s)) (cons (car s)
                            (filter fn (cdr s))))
        (else (filter fn (cdr s)))))

; Implementing and using these helper procedures is optional. You are allowed
; to delete them.
(define (unique s)
  'YOUR-CODE-HERE
  nil
)

(define (count name s)
  'YOUR-CODE-HERE
  nil
)

(define (tally names)
  'YOUR-CODE-HERE
  nil
)

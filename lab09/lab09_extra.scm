;; Extra Scheme Questions ;;


; Q5
(define lst
  'YOUR-CODE-HERE
)

; Q6
(define (composed f g)
  'YOUR-CODE-HERE
  (lambda (x) (f (g x)))
)

; Q7
(define (remove item lst)
  'YOUR-CODE-HERE
  (define (have? x y)
    (if (= x y)
        #f
        #t))
  (define (filter f lst x)
    (if (null? lst)
        nil
        (if (f (car lst) x)
            (cons (car lst) (filter f (cdr lst) x))
            (filter f (cdr lst) x))))
  (filter have? lst item)
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q8
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  'YOUR-CODE-HERE
  (if (= b 0)
      a
      (gcd b (modulo a b)))
)

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q9
(define (no-repeats s)
  'YOUR-CODE-HERE
  (define (count lst x)
    (if (null? lst)
        0
        (if (= (car lst) x)
            (+ 1 (count (cdr lst) x))
            (count (cdr lst) x))))
  (define (filter f lst)
    (if (null? lst)
        nil
        (if (= (f lst (car lst)) 1)
            (cons (car lst) (filter f (cdr lst)))
            (filter f (cdr lst)))))
  (filter count s)
)

; Q10
(define (substitute s old new)
  'YOUR-CODE-HERE
  (if (null? s)
      nil
      (if (pair? (car s))
          (cons (substitute (car s) old new) (substitute (cdr s) old new))
          (if (eq? (car s) old)
              (cons new (substitute (cdr s) old new))
              (cons (car s) (substitute (cdr s) old new)))))
)

; Q11
(define (sub-all s olds news)
  'YOUR-CODE-HERE
  (if (null? s)
      nil
      (if (null? olds)
          s
          (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news))))
)

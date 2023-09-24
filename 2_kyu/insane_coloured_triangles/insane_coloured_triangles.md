# Insane Coloured Triangles

## Theory

With identical

[exam paper](https://www.olympiad.org.uk/papers/2017/bio/bio17-exam.pdf]

> _If the first row contains 4 squares, the colour of the square in the final row only depends on the extreme left and
right of the first row._


Don't worry, we don't have to look at all 3 ** 4 = 81 possible combinations.



    R R R R     R R G R     R G B R
     R R R       R B B       B R G
      R R         G B         G B
       R           R           R

    R R R G     
     R R B
      R G
       B

> _If the first row contains more than 4 squares, the colour of the square in the final row only depends on the extreme left and
right of the row with 4 squares._


> _Every square that is not in the first row is the bottom of at least some triangle with a size of 3 ** k + 1 for some k._

The [solutions](hhttps://www.olympiad.org.uk/papers/2017/bio/bio17-marks.pdf) tell us that this also holds for `n = 10`
and, indeed, any `n = 3 ** k + 1` where `k > 1`. The purpose of the restriction `k > 1`, of course, is that the question
asks for some `n > 4` - but we already know that `k = 1` and `k = 0` also give us the desired result.

     G B B B B R B G R B R R G B R
      . . . . . . . . . . . . . .
       . . . . . . . . . . . . .
        . . . . . . . . . . . .
         . . . . . . . . . . .
          . . . . . . . . . .
           . . . . . . . . .
            . . . . . . . .
             . . . . . . .
              . . . . . .
               . . . . .
                . . . .
                 . . .
                  . .
                   ?

     G B B B B R B G R B R R G B R
      . . . . . . . . . . . . . .
       . . . . . . . . . . . . .
        . . . . . . . . . . . .
         . . . . . . . . . . .
          ? . . . . . . . . ?
           . . . . . . . . .
            . . . . . . . .
             . . . . . . .
              . . . . . .
               . . . . .
                . . . .
                 . . .
                  . .
                   ?

    
     G B B B B R B G R B R R G B R
      . . . . . . . . . . . . . .
       . . . . . . . . . . . . .
        . . . . . . . . . . . .
         . . . . . . . . . . .
          ? . . . . . . . . ?
           . . . . . . . . .
            . . . . . . . .
             . . . . . . .
              . . . . . .
               . . . . .
                . . . .
                 . . .
                  . .
                   ?


     G B B B B R B G R B R R G B R
      ? ? . ? ? . . . . ? ? . ? ?
       ? . . ? . . . . . ? . . ?
        . . . . . . . . . . . .
         . . . . . . . . . . .
          ? . . . . . . . . ?
           . . . . . . . . .
            . . . . . . . .
             . . . . . . .
              . . . . . .
               . . . . .
                . . . .
                 . . .
                  . .
                   ?

     G B B B B R B G R B R R G B R
      R B . B G . . . . G R . R G
       ? . . ? . . . . . ? . . ?
        . . . . . . . . . . . .
         . . . . . . . . . . .
          ? . . . . . . . . ?
           . . . . . . . . .
            . . . . . . . .
             . . . . . . .
              . . . . . .
               . . . . .
                . . . .
                 . . .
                  . .
                   ?

     G B B B B R B G R B R R G B R
      R B . B G . . . . G R . R G
       G . . R . . . . . B . . B
        . . . . . . . . . . . .
         . . . . . . . . . . .
          ? . . . . . . . . ?
           . . . . . . . . .
            . . . . . . . .
             . . . . . . .
              . . . . . .
               . . . . .
                . . . .
                 . . .
                  . .
                   ?

     G B B B B R B G R B R R G B R
      R B . B G . . . . G R . R G
       G . . R . . . . . B . . B
        . . . . . . . . . . . .
         . . . . . . . . . . .
          B . . . . . . . . B
           . . . . . . . . .
            . . . . . . . .
             . . . . . . .
              . . . . . .
               . . . . .
                . . . .
                 . . .
                  . .
                   ?

     G B B B B R B G R B R R G B R
      R B . B G . . . . G R . R G
       G . . R . . . . . B . . B
        . . . . . . . . . . . .
         . . . . . . . . . . .
          B . . . . . . . . B
           . . . . . . . . .
            . . . . . . . .
             . . . . . . .
              . . . . . .
               . . . . .
                . . . .
                 . . .
                  . .
                   B


## Implementation

Since it is stipulated that `1 <= length(row) <= 10 ** 5` and there are only 11 different numbers `n = 3 ** k + 1`
(excluding `3 ** 0 = 1`) in that range, 


    limit = 10 ** 5
    powers_of_3_plus_1 = []
    power_of_3 = 1
    while power_of_3 < limit:
        powers_of_3_plus_1.append(power_of_3 + 1)
        power_of_3 *= 3
    powers_of_3.reverse()

This gives us `powers_of_3 = [177147, 59049, 19683, 6561, 2187, 729, 243, 81, 27, 9, 3, 1]`.


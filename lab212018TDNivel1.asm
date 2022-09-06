.data
a: .word 0xfffffffa, 0x00000004, 0x00000010
b: .word 3, 2, 1

.text
li $t0, 0x10010000
lw $t1, 0($t0)
lw $t2,4($t0)
lw $t3, 8($t0)
add $t1, $t2, $t3
xor $t4, $t1, $t2
sub $t5, $t3, $t2
or $t4, $t5, $t1
nor $t4,$t4, $t1
addi $t5, $t4, 10
xori $t6, $t5, 20
sw $t4, 0($t0)
sw $t5, 4($t0)
sw $t6, 8($t0)

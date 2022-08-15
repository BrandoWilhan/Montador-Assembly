.data
a: .word 9, 8, 7, 6, 5

.text
addi $t1, $zero, 0x10010000
lw $t1, 0($t1)
xor $t1, $zero, $t1
addi $t1, $zero, 0x10010000
lw $t1, 4($t1)
sll $t1,$t1,31
li $t1, -1000
subu $t1, $zero, $t1
addi $t1, $zero, 0x10010000
lw $t1, 8($t1)
mult $t1, $t1
mflo $t1
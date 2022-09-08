.data
a:	 .word	1,2,3,4,5,6,7,8,9,10
.text
Mm: 	li 	$t1, 32
	li 	$s0,0
L1: 	li 	$s1,0
L2: 	li 	$s2,0
	sll 	$t2,$s0,5  
	addu 	$t2,$t2,$s1
	sll 	$t2,$t2,3
	addu 	$t2, $a0, $t2
	L3: 	sll $t0,$s0,5
	addu 	$t0,$t0,$s2
	sll 	$t0,$t0,3
	addu 	$t0, $a1, $t0
	sll 	$t0,$s2,5
	addu 	$t0,$t0,$s1
	sll 	$t0,$t0,3
	addu 	$t0, $a2, $t0
	addiu 	$s2,$s2,1
	bne 	$s2, $t1, L3
	addiu 	$s1,$s1,1
	bne 	$s1,$t1, L2
	addiu 	$s0,$s0,1
	bne 	$s0,$t1,L1
.data
str_nl: .asciz "\n"
.text
j Lmain
# 0 : begin_block , αύξηση3 , _ , _
sw ra, (sp)
# 1 : + , α , 1 , t@1
lw t1, -12(sp)
li t2, 1
add t1, t1, t2
sw t1, -20(sp)
# 2 : := , t@1 , _ , β
lw t1, -20(sp)
lw t0, -16(gp)
sw t1, (t0)
# 3 : + , α , 1 , t@2
lw t1, -12(sp)
li t2, 1
add t1, t1, t2
sw t1, -24(sp)
# 4 : retv , t@2 , _ , _
lw t1, -24(sp)
lw t0, -8(sp)
sw t1, (t0)
# 5 : end_block , αύξηση3 , _ , _
lw ra, (sp)
jr ra
# 6 : begin_block , αύξηση2 , _ , _
sw ra, (sp)
# 7 : + , α , 1 , t@3
lw t1, -12(sp)
li t2, 1
add t1, t1, t2
sw t1, -20(sp)
# 8 : := , t@3 , _ , β
lw t1, -20(sp)
lw t0, -16(gp)
sw t1, (t0)
# 9 : + , α , 1 , t@4
lw t1, -12(sp)
li t2, 1
add t1, t1, t2
sw t1, -24(sp)
# 10 : retv , t@4 , _ , _
lw t1, -24(sp)
lw t0, -8(sp)
sw t1, (t0)
# 11 : end_block , αύξηση2 , _ , _
lw ra, (sp)
jr ra
# 12 : begin_block , τύπωσε_συν_1 , _ , _
sw ra, (sp)
# 13 : + , χ , 1 , t@5
lw t1, -12(sp)
li t2, 1
add t1, t1, t2
sw t1, -16(sp)
# 14 : end_block , τύπωσε_συν_1 , _ , _
lw ra, (sp)
jr ra
# 15 : begin_block , αύξηση , _ , _
sw ra, (sp)
# 16 : + , α , 1 , t@6
lw t1, -12(sp)
li t2, 1
add t1, t1, t2
sw t1, -20(sp)
# 17 : := , t@6 , _ , β
lw t1, -20(sp)
lw t0, -16(gp)
sw t1, (t0)
# 18 : + , α , 1 , t@7
lw t1, -12(sp)
li t2, 1
add t1, t1, t2
sw t1, -24(sp)
# 19 : retv , t@7 , _ , _
lw t1, -24(sp)
lw t0, -8(sp)
sw t1, (t0)
# 20 : end_block , αύξηση , _ , _
lw ra, (sp)
jr ra
# 21 : begin_block , αύξηση3 , _ , _
sw ra, (sp)
# 22 : + , α , 1 , t@8
lw t1, -12(sp)
li t2, 1
add t1, t1, t2
sw t1, -20(sp)
# 23 : := , t@8 , _ , β
lw t1, -20(sp)
lw t0, -16(gp)
sw t1, (t0)
# 24 : + , α , 1 , t@9
lw t1, -12(sp)
li t2, 1
add t1, t1, t2
sw t1, -24(sp)
# 25 : retv , t@9 , _ , _
lw t1, -24(sp)
lw t0, -8(sp)
sw t1, (t0)
# 26 : end_block , αύξηση3 , _ , _
lw ra, (sp)
jr ra
# 27 : begin_block , τύπωσε_συν_1 , _ , _
sw ra, (sp)
# 28 : + , χ , 1 , t@10
lw t1, -12(sp)
li t2, 1
add t1, t1, t2
sw t1, -16(sp)
# 29 : end_block , τύπωσε_συν_1 , _ , _
lw ra, (sp)
jr ra
# 30 : begin_block , τύπωσε_συν_1 , _ , _
sw ra, (sp)
# 31 : + , χ , 1 , t@11
lw t1, -12(sp)
li t2, 1
add t1, t1, t2
sw t1, -16(sp)
# 32 : end_block , τύπωσε_συν_1 , _ , _
lw ra, (sp)
jr ra
# 33 : begin_block , τεστ , _ , _
Lmain:
addi sp, sp, 0
mv gp, sp
# 34 : := , 1 , _ , α
li t1, 1
sw t1, -12(gp)
# 35 : * , α , α , t@12
lw t1, -12(gp)
lw t2, -12(gp)
mul t1, t1, t2
sw t1, -24(gp)
# 36 : - , 2 , α , t@13
li t1, 2
lw t2, -12(gp)
sub t1, t1, t2
sw t1, -28(gp)
# 37 : * , 2 , α , t@14
li t1, 2
lw t2, -12(gp)
mul t1, t1, t2
sw t1, -32(gp)
# 38 : - , t@13 , t@14 , t@15
lw t1, -28(gp)
lw t2, -32(gp)
sub t1, t1, t2
sw t1, -36(gp)
# 39 : / , t@12 , t@15 , t@16
lw t1, -24(gp)
lw t2, -36(gp)
div t1, t1, t2
sw t1, -40(gp)
# 40 : + , 2 , t@16 , t@17
li t1, 2
lw t2, -40(gp)
add t1, t1, t2
sw t1, -44(gp)
# 41 : := , t@17 , _ , β
lw t1, -44(gp)
sw t1, -16(gp)
# 42 : par , α , CV , _
addi fp, sp, 28
lw t0, -12(gp)
sw t0, -12(fp)
# 43 : par , β , REF , _
# 44 : par , t@18 , RET , _
addi t0, sp, -20
sw t0, -8(fp)
# 45 : call , αύξηση , _ , _
sw sp, -4(fp)
addi sp, sp, 28
jal L15
addi sp, sp, -28
# 46 : := , t@18 , _ , γ
lw t1, -48(gp)
sw t1, -20(gp)
# 47 : := , 1 , _ , α
li t1, 1
sw t1, -12(gp)
# 48 : jump , _ , _ , 50
j L50
# 49 : + , α , -2 , α
lw t1, -12(gp)
li t2, -2
add t1, t1, t2
sw t1, -12(gp)
# 50 : < , -2 , 0 , 53
li t1, -2
li t2, 0
blt t1, t2, L53
# 51 : > , -2 , 0 , 55
li t1, -2
li t2, 0
bgt t1, t2, L55
# 52 : jump , _ , _ , 57
j L57
# 53 : >= , α , 8 , 57
lw t1, -12(gp)
li t2, 8
bge t1, t2, L57
# 54 : jump , _ , _ , 60
j L60
# 55 : <= , α , 8 , 57
# 56 : jump , _ , _ , 60
j L60
# 57 : par , α , CV , _
addi fp, sp, 20
lw t0, -12(gp)
sw t0, -12(fp)
# 58 : call , τύπωσε_συν_1 , _ , _
sw sp, -4(fp)
addi sp, sp, 20
jal L30
addi sp, sp, -20
# 59 : jump , _ , _ , 49
j L49
# 60 : := , 1 , _ , β
li t1, 1
sw t1, -16(gp)
# 61 : <> , β , 22 , 67
lw t1, -16(gp)
li t2, 22
bne t1, t2, L67
# 62 : jump , _ , _ , 63
j L63
# 63 : >= , β , 23 , 70
lw t1, -16(gp)
li t2, 23
bge t1, t2, L70
# 64 : jump , _ , _ , 65
j L65
# 65 : <= , β , 24 , 70
# 66 : jump , _ , _ , 67
j L67
# 67 : + , β , 1 , t@19
lw t1, -16(gp)
li t2, 1
add t1, t1, t2
sw t1, -52(gp)
# 68 : := , t@19 , _ , β
lw t1, -52(gp)
sw t1, -16(gp)
# 69 : jump , _ , _ , 72
j L72
# 70 : - , β , 1 , t@20
lw t1, -16(gp)
li t2, 1
sub t1, t1, t2
sw t1, -56(gp)
# 71 : := , t@20 , _ , β
lw t1, -56(gp)
sw t1, -16(gp)
# 72 : := , 1 , _ , β
li t1, 1
sw t1, -16(gp)
# 73 : <> , β , 22 , 79
lw t1, -16(gp)
li t2, 22
bne t1, t2, L79
# 74 : jump , _ , _ , 75
j L75
# 75 : >= , β , 23 , 82
lw t1, -16(gp)
li t2, 23
bge t1, t2, L82
# 76 : jump , _ , _ , 77
j L77
# 77 : <= , β , 24 , 82
# 78 : jump , _ , _ , 79
j L79
# 79 : + , β , 1 , t@21
lw t1, -16(gp)
li t2, 1
add t1, t1, t2
sw t1, -60(gp)
# 80 : := , t@21 , _ , β
lw t1, -60(gp)
sw t1, -16(gp)
# 81 : jump , _ , _ , 82
j L82
# 82 : < , β , 10 , 84
lw t1, -16(gp)
li t2, 10
blt t1, t2, L84
# 83 : jump , _ , _ , 94
j L94
# 84 : <> , β , 22 , 90
lw t1, -16(gp)
li t2, 22
bne t1, t2, L90
# 85 : jump , _ , _ , 86
j L86
# 86 : >= , β , 23 , 88
lw t1, -16(gp)
li t2, 23
bge t1, t2, L88
# 87 : jump , _ , _ , 93
j L93
# 88 : <= , β , 24 , 90
# 89 : jump , _ , _ , 93
j L93
# 90 : + , β , 1 , t@22
lw t1, -16(gp)
li t2, 1
add t1, t1, t2
sw t1, -64(gp)
# 91 : := , t@22 , _ , β
lw t1, -64(gp)
sw t1, -16(gp)
# 92 : jump , _ , _ , 93
j L93
# 93 : jump , _ , _ , 82
j L82
# 94 : inp , β , _ , _
li a7, 5
ecall
mv t1, a0
sw t1, -16(gp)
# 95 : + , β , 1 , t@23
lw t1, -16(gp)
li t2, 1
add t1, t1, t2
sw t1, -68(gp)
# 96 : := , t@23 , _ , β
lw t1, -68(gp)
sw t1, -16(gp)
# 97 : < , β , -100 , 95
lw t1, -16(gp)
li t2, -100
blt t1, t2, L95
# 98 : jump , _ , _ , 99
j L99
# 99 : halt , _ , _ , _

def lexico(codigo):
    codigo = codigo + " "
    n = len(codigo)
    i = 0
    tokens = []
    estado = 0
    lexema = ""

    while i < n:
        c = codigo[i]
        
        # ==================== ESTADO 0: INICIAL ====================
        if estado == 0:
            # ---------- PALABRAS RESERVADAS ----------
            if codigo[i:i+8] == 'declarar':
                estado = -1
                i += 8
                continue
            elif codigo[i:i+6] == 'entero':
                estado = -2
                i += 6
                continue
            elif codigo[i:i+4] == 'real':
                estado = -3
                i += 4
                continue
            elif codigo[i:i+6] == 'cadena':
                estado = -4
                i += 6
                continue
            elif codigo[i:i+8] == 'booleano':
                estado = -5
                i += 8
                continue
            elif codigo[i:i+4] == 'leer':
                estado = -6
                i += 4
                continue
            elif codigo[i:i+7] == 'escribir':
                estado = -7
                i += 7
                continue
            elif codigo[i:i+2] == 'si' and (i+2 >= n or not codigo[i+2].isalpha()):
                estado = -8
                i += 2
                continue
            elif codigo[i:i+7] == 'entonces':
                estado = -9
                i += 7
                continue
            elif codigo[i:i+4] == 'sino':
                estado = -10
                i += 4
                continue
            elif codigo[i:i+5] == 'fin si':
                estado = -11
                i += 5
                continue
            elif codigo[i:i+8] == 'mientras':
                estado = -12
                i += 8
                continue
            elif codigo[i:i+11] == 'fin mientras':
                estado = -13
                i += 11
                continue
            elif codigo[i:i+7] == 'funcion':
                estado = -14
                i += 7
                continue
            elif codigo[i:i+11] == 'fin funcion':
                estado = -15
                i += 11
                continue
            elif codigo[i:i+8] == 'retornar':
                estado = -16
                i += 8
                continue
            elif codigo[i:i+1] == 'y' and (i+1 >= n or not codigo[i+1].isalpha()):
                estado = -17
                i += 1
                continue
            elif codigo[i:i+1] == 'o' and (i+1 >= n or not codigo[i+1].isalpha()):
                estado = -18
                i += 1
                continue
            elif codigo[i:i+2] == 'no' and (i+2 >= n or not codigo[i+2].isalpha()):
                estado = -19
                i += 2
                continue
            elif codigo[i:i+9] == 'verdadero':
                estado = -20
                i += 9
                continue
            elif codigo[i:i+5] == 'falso':
                estado = -21
                i += 5
                continue
            
            # ---------- OPERADORES (2 caracteres) ----------
            elif codigo[i:i+2] == '>=':
                estado = -40
                i += 2
                continue
            elif codigo[i:i+2] == '<=':
                estado = -41
                i += 2
                continue
            elif codigo[i:i+2] == '==':
                estado = -42
                i += 2
                continue
            elif codigo[i:i+2] == '!=':
                estado = -43
                i += 2
                continue
            
            # ---------- SÍMBOLOS Y OPERADORES (1 carácter) ----------
            elif c == '+':
                estado = -44
                i += 1
                continue
            elif c == '-':
                estado = -45
                i += 1
                continue
            elif c == '*':
                estado = -46
                i += 1
                continue
            elif c == '/':
                estado = -47
                i += 1
                continue
            elif c == '%':
                estado = -48
                i += 1
                continue
            elif c == '>':
                estado = -49
                i += 1
                continue
            elif c == '<':
                estado = -50
                i += 1
                continue
            elif c == '=':
                estado = -51
                i += 1
                continue
            elif c == ',':
                estado = -52
                i += 1
                continue
            elif c == ':':
                estado = -53
                i += 1
                continue
            elif c == ';':
                estado = -54
                i += 1
                continue
            elif c == '(':
                estado = -55
                i += 1
                continue
            elif c == ')':
                estado = -56
                i += 1
                continue
            
            # ---------- CADENAS ----------
            elif c == '"':
                lexema = c
                i += 1
                estado = 7
                continue
            
            # ---------- NÚMEROS ----------
            elif c.isdigit():
                lexema = c
                i += 1
                estado = 3
                continue
            
            # ---------- IDENTIFICADORES ----------
            elif c.isalpha():
                lexema = c
                i += 1
                estado = 4
                continue
            
            # ---------- ESPACIOS ----------
            elif c.isspace():
                i += 1
            
            # ---------- ERROR ----------
            else:
                return f'ERROR LEXICO: Caracter "{c}" no valido'
        
        # ==================== ESTADO 3: NÚMERO ENTERO ====================
        elif estado == 3:
            if c.isdigit():
                lexema += c
                i += 1
                estado = 3
            elif c == '.':
                lexema += c
                i += 1
                estado = 5
            else:
                tokens.append(700)  # ENTERO
                estado = 0
        
        # ==================== ESTADO 4: IDENTIFICADOR ====================
        elif estado == 4:
            if c.isalpha() or c.isdigit() or c == '_':
                lexema += c
                i += 1
                estado = 4
            else:
                tokens.append(1000)  # IDENTIFICADOR
                lexema = ""
                estado = 0
        
        # ==================== ESTADO 5: PUNTO DECIMAL ====================
        elif estado == 5:
            if c.isdigit():
                lexema += c
                i += 1
                estado = 6
            else:
                return 'ERROR LEXICO: Se esperaba digito despues del punto'
        
        # ==================== ESTADO 6: PARTE FRACCIONARIA ====================
        elif estado == 6:
            if c.isdigit():
                lexema += c
                i += 1
                estado = 6
            else:
                tokens.append(701)  # REAL
                lexema = ""
                estado = 0
        
        # ==================== ESTADO 7: CADENA ====================
        elif estado == 7:
            if c == '"':
                tokens.append(702)  # CADENA
                estado = 0
                i += 1
            else:
                lexema += c
                i += 1
                estado = 7
        
        # ==================== ESTADOS NEGATIVOS (EMISIÓN DE TOKENS) ====================
        elif estado == -1:   # declarar
            tokens.append(201); estado = 0
        elif estado == -2:   # entero
            tokens.append(202); estado = 0
        elif estado == -3:   # real
            tokens.append(203); estado = 0
        elif estado == -4:   # cadena
            tokens.append(204); estado = 0
        elif estado == -5:   # booleano
            tokens.append(205); estado = 0
        elif estado == -6:   # leer
            tokens.append(206); estado = 0
        elif estado == -7:   # escribir
            tokens.append(207); estado = 0
        elif estado == -8:   # si
            tokens.append(208); estado = 0
        elif estado == -9:   # entonces
            tokens.append(209); estado = 0
        elif estado == -10:  # sino
            tokens.append(210); estado = 0
        elif estado == -11:  # fin si
            tokens.append(211); estado = 0
        elif estado == -12:  # mientras
            tokens.append(212); estado = 0
        elif estado == -13:  # fin mientras
            tokens.append(213); estado = 0
        elif estado == -14:  # funcion
            tokens.append(214); estado = 0
        elif estado == -15:  # fin funcion
            tokens.append(215); estado = 0
        elif estado == -16:  # retornar
            tokens.append(216); estado = 0
        elif estado == -17:  # y
            tokens.append(217); estado = 0
        elif estado == -18:  # o
            tokens.append(218); estado = 0
        elif estado == -19:  # no
            tokens.append(219); estado = 0
        elif estado == -20:  # verdadero
            tokens.append(703); estado = 0
        elif estado == -21:  # falso
            tokens.append(704); estado = 0
        
        # Estados para operadores y símbolos
        elif estado == -40:  # >=
            tokens.append(307); estado = 0
        elif estado == -41:  # <=
            tokens.append(308); estado = 0
        elif estado == -42:  # ==
            tokens.append(309); estado = 0
        elif estado == -43:  # !=
            tokens.append(310); estado = 0
        elif estado == -44:  # +
            tokens.append(300); estado = 0
        elif estado == -45:  # -
            tokens.append(301); estado = 0
        elif estado == -46:  # *
            tokens.append(302); estado = 0
        elif estado == -47:  # /
            tokens.append(303); estado = 0
        elif estado == -48:  # %
            tokens.append(304); estado = 0
        elif estado == -49:  # >
            tokens.append(305); estado = 0
        elif estado == -50:  # <
            tokens.append(306); estado = 0
        elif estado == -51:  # =
            tokens.append(403); estado = 0
        elif estado == -52:  # ,
            tokens.append(400); estado = 0
        elif estado == -53:  # :
            tokens.append(401); estado = 0
        elif estado == -54:  # ;
            tokens.append(402); estado = 0
        elif estado == -55:  # (
            tokens.append(404); estado = 0
        elif estado == -56:  # )
            tokens.append(405); estado = 0
    
    return tokens


codigo = '''
            funcion esPar(n: entero): entero
            si n % 2 = 0 entonces
            retornar 1
                sino
                    retornar 0
            fin si
            fin funcion
    
            declarar numero: entero
            declarar texto: cadena
            texto = "Ingrese un numero: "
            escribir texto
            leer numero
            si esPar(numero) = 1 entonces
            escribir "El numero ", numero, " es par"
            sino
            escribir "El numero ", numero, " es impar"
            fin si
    '''

print(lexico(codigo))  

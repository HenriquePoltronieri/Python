import math
from flask import render_template, request

def calcular():
    num1 = float(request.form["num1"])
    operacao = request.form["operacao"]

    if operacao == "bhaskara":
        num2_valor = request.form.get("num2", "").strip()
        num3_valor = request.form.get("num3", "").strip() 

        if not num2_valor or not num3_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe os coeficientes B e C para a equação de Bhaskara.",
                resultados="",
            )

        a = num1
        b = float(num2_valor)
        c = float(num3_valor)

        if a == 0:
            return render_template(
                "calculadora.html",
                etapas="O coeficiente 'A' não pode ser zero em uma equação de 2º grau.",
                resultados="Erro",
            )

        delta = (b ** 2) - (4 * a * c)
        etapas_lista = [
            f"Equação: {a}x² + ({b})x + ({c}) = 0",
            f"Δ = b² - 4ac",
            f"Δ = ({b})² - 4 * {a} * {c}",
            f"Δ = {delta}"
        ]

        if delta < 0:
            resultado = "Sem raízes reais"
            etapas_lista.append("Como o Delta é negativo, não existem raízes reais.")
        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            resultado = f"x₁ = {x1} | x₂ = {x2}"
            etapas_lista.append(f"x = (-b ± √Δ) / 2a")
            etapas_lista.append(f"x₁ = (-({b}) + √{delta}) / (2 * {a}) = {x1}")
            etapas_lista.append(f"x₂ = (-({b}) - √{delta}) / (2 * {a}) = {x2}")

        etapas_finais = "<br>".join(etapas_lista)

        return render_template(
            "calculadora.html",
            etapas=etapas_finais,
            resultados=resultado
        )

    if operacao == "sqrt":
        if num1 < 0:
            resultado = "Erro"
            etapas = f"Não existe raiz real de número negativo ({num1})."
        else:
            resultado = math.sqrt(num1)
            etapas = f"√{num1} = {resultado}"
            
    elif operacao == "log":
        if num1 <= 0:
            resultado = "Erro"
            etapas = f"Não existe logaritmo de número menor ou igual a zero ({num1})."
        else:
            resultado = math.log(num1)
            etapas = f"ln({num1}) = {resultado}"

    else:
        num2_valor = request.form.get("num2", "").strip()
        if not num2_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o segundo número para esta operação.",
                resultados="",
            )
        num2 = float(num2_valor)

        if operacao == "+":
            resultado = num1 + num2
            etapas = f"{num1} + {num2} = {resultado}"
            
        elif operacao == "-":
            resultado = num1 - num2
            etapas = f"{num1} - {num2} = {resultado}"
            
        elif operacao == "*":
            resultado = num1 * num2
            etapas = f"{num1} * {num2} = {resultado}"
            
        elif operacao == "/":
            if num2 == 0:
                resultado = "Erro"
                etapas = "Divisão por zero não é permitida."
            else:
                resultado = num1 / num2
                etapas = f"{num1} ÷ {num2} = {resultado}"
                
        elif operacao == "**":
            resultado = num1 ** num2
            etapas = f"{num1} ^ {num2} = {resultado}"
            
        else:
            resultado = "Erro"
            etapas = "Operação inválida."

    return render_template(
        "calculadora.html",
        etapas=etapas,
        resultados=resultado
    )

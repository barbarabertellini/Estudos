manutencao = input("DIgite o valor da manutenção do veículo: ")
manutencao = float(manutencao)

impostoservicos = input("Digite a porcentagem dos impostos de serviços: ")
impostoservicos = float(impostoservicos)

impostosprodutos = input("Digite a porcentagem dos impostos de produto: ")
impostosprodutos = float(impostosprodutos)

print("O total de impostos a serem pagos por serviço é de", impostoservicos * manutencao, "reais")
print("O total de impostos a serem pagos por produto é de", impostosprodutos * manutencao, "reais")
total = (impostoservicos * manutencao) + (impostosprodutos * manutencao)
print("O valor total após os descontos é de", manutencao - total, "reais")
seconde=int(input("veuillez saisir un nombres de second :"))
heures = seconde // 3600

r=seconde%3600

muni=r//60

second=seconde%60
print(seconde," fait",heures,": heures", "et :",muni," minutes", second," :secondes ", )
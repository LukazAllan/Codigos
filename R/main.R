while (i <= 168) {
  if (data[i,6] > data[i,5] && data[i,6] > data[i,4] && data[i,6] > data[i,3] && data[i,6] > data[i,2]){
    ce_br <- ce_br + 1
  } else {
    if (data[i,5] > data[i,6] && data[i,5] > data[i,4] && data[i,5] > data[i,3] && data[i,5] > data[i,2]){
      ce_jo <- ce_jo + 1
    } else {
      if (data[i,4] > data[i,6] && data[i,4] > data[i,5] && data[i,4] > data[i,3] && data[i,4] > data[i,2]){
        ce_ce <- ce_ce + 1
      } else {
        if (data[i,3] > data[i,6] && data[i,3] > data[i,5] && data[i,3] > data[i,4] && data[i,3] > data[i,2]){
          ce_bo <- ce_bo + 1
        } else {
          ce_ar <- ce_ar + 1

        }
      }
    }
  }
  i <- i + 1
}

while (i <= 182) {
  if (data1[i,6] > data1[i,5] && data1[i,6] > data1[i,4] && data1[i,6] > data1[i,3] && data1[i,6] > data1[i,2]){
    ce_br <- ce_br + 1
  } else {
    if (data1[i,5] > data1[i,6] && data1[i,5] > data1[i,4] && data1[i,5] > data1[i,3] && data1[i,5] > data1[i,2]){
      ce_jo <- ce_jo + 1
    } else {
      if (data1[i,4] > data1[i,6] && data1[i,4] > data1[i,5] && data1[i,4] > data1[i,3] && data1[i,4] > data1[i,2]){
        ce_ce <- ce_ce + 1
      } else {
        if (data1[i,3] > data1[i,6] && data1[i,3] > data1[i,5] && data1[i,3] > data1[i,4] && data1[i,3] > data1[i,2]){
          ce_bo <- ce_bo + 1
        } else {
          ce_ar <- ce_ar + 1

        }
      }
    }
  }
  i <- i + 1
}
#data[i,6] br
#data[i,5] jo
#data[i,4] ce
#data[i,3] bo
#data[i,2] ar
names <- c("Arthur do Val", "Guilherme Boulos", "Bruno Covas", "Celso Russomano", "Joice Hasselmann", "Márcio França","Marina Helou","Orlando Silva", "Levy Fidelix","Antonio Carlos","Jilmar Tatto")
cores = c(          "blue",              "red",      "purple",          "yellow",             "pink",        "orange",       "green",        "black",        "white",          "gray",        "gray")

tot <- c(tot_ar, tot_bo, tot_br, tot_ce, tot_jo)
tb <- table(tot, names)
tb
tb <- table(tot, label = names)
tb
pie(tot, labels = names)
sum(tot)
pct <- round(tot/sum(tot)*100)
lbls <- paste(names, pct)
lbls <- paste(names, "%",sep = "")
pie(tot, labels = names)
pie(tot, labels = lbls)
lbls <- names
lbls <- paste(names, pct)
lbls <- paste(names, "%",sep = "")
lbls <- names
lbls <- paste(names, pct, "%",sep = "")
lbls <- paste(names, pct, "%",sep = " ")
lbls <- paste(names, " ", pct, "%",sep = "")
pie(tot, labels = lbls)
pie(tot, labels = lbls, col = rainbow(length(lbls)), main = "Pesquisas nos Últimos 7 dias")
pie(tot, labels = lbls, col = c("blue", "red", "purple", "yellow", "orange"), main = "Pesquisas nos Últimos 7 dias")
cores = c("blue", "red", "purple", "yellow", "orange")

ce <- c(ce_ar, ce_bo, ce_br, ce_ce, ce_jo)
pct <- round(ce/sum(ce)*100)
lbls <- paste(names, " ", pct, "%",sep = "")
pie(ce, labels = lbls, col = cores, main = "Pesquisa do dia em 7 dias e 30 dias")

barplot(ce, legend = names, col = cores, main = "Pesquisa do dia em 7 dias e 30 dias")
barplot(ce, legend = c("AV", "GB", "BC", "CR", "JH"), col = cores, main = "Pesquisa do dia em 7 dias e 30 dias")
barplot(ce, legend = names, xlab = "Candidatos", ylab = "Vezes que foi o mais pesquisado",col = cores, main = "Pesquisa do dia em 7 dias e 30 dias")
c("Arthur do Val", "Guilherme Boulos", "Bruno Covas", "Celso Russomano", "Joice Hasselmann")

j = 1
ce_ar <- 0
ce_bo <- 0
ce_br <- 0
ce_ce <- 0
ce_jo <- 0
arq = c("Allan/Dados/p_sp_2020_11_14_15_21.csv",
          "Allan/Dados/p_sp_2020_11_14_16_21.csv",
          "Allan/Dados/p_sp_2020_11_14_17_21.csv",
          "Allan/Dados/p_sp_2020_11_14_18_21.csv",
          "Allan/Dados/p_sp_2020_11_14_19_21.csv",
          "Allan/Dados/p_sp_2020_11_14_20_21.csv",
          "Allan/Dados/p_sp_2020_11_14_21_27.csv",
          "Allan/Dados/p_sp_2020_11_14_22_07.csv",
          "Allan/Dados/p_sp_2020_11_14_23_43.csv"
          )
while (j < 10) {
  datum = read.csv(arq[j], TRUE)
  i=1
  while (i <= 61) {
    if (data1[i,6] > data1[i,5] && data1[i,6] > data1[i,4] && data1[i,6] > data1[i,3] && data1[i,6] > data1[i,2]){
      ce_br <- ce_br + 1
    } else {
      if (data1[i,5] > data1[i,6] && data1[i,5] > data1[i,4] && data1[i,5] > data1[i,3] && data1[i,5] > data1[i,2]){
        ce_jo <- ce_jo + 1
      } else {
        if (data1[i,4] > data1[i,6] && data1[i,4] > data1[i,5] && data1[i,4] > data1[i,3] && data1[i,4] > data1[i,2]){
          ce_ce <- ce_ce + 1
        } else {
          if (data1[i,3] > data1[i,6] && data1[i,3] > data1[i,5] && data1[i,3] > data1[i,4] && data1[i,3] > data1[i,2]){
            ce_bo <- ce_bo + 1
          } else {
            ce_ar <- ce_ar + 1

          }
        }
      }
    }
    i <- i + 1
  }
  j <- j + 1
}
ce <- c(ce_ar, ce_bo, ce_br, ce_ce, ce_jo)
pct <- round(ce/sum(ce)*100)
lbls <- paste(names, " ", pct, "%",sep = "")
barplot(ce, legend = names, xlab = "Candidatos", ylab = "Vezes que foi o mais pesquisado",col = cores, main = "Pesquisa do dia 14 entre 15h20 às 23h40")


tot_ar <- 0
tot_bo <- 0
tot_br <- 0
tot_ce <- 0
tot_jo <- 0
arq = c("Allan/Dados/p_sp_2020_11_14_15_21.csv",
        "Allan/Dados/p_sp_2020_11_14_16_21.csv",
        "Allan/Dados/p_sp_2020_11_14_17_21.csv",
        "Allan/Dados/p_sp_2020_11_14_18_21.csv",
        "Allan/Dados/p_sp_2020_11_14_19_21.csv",
        "Allan/Dados/p_sp_2020_11_14_20_21.csv",
        "Allan/Dados/p_sp_2020_11_14_21_27.csv",
        "Allan/Dados/p_sp_2020_11_14_22_07.csv",
        "Allan/Dados/p_sp_2020_11_14_23_43.csv"
)
j = 1
fim = 181
while (j < 2) {
  i=1
  while (i < fim) {
    tot_ar <- tot_ar + data1[i,2]
    i <- i + 1
  }

  i=1
  while (i < fim) {
    tot_bo <- tot_bo + data1[i,3]
    i <- i + 1
  }

  i=1
  while (i < fim) {
    tot_ce <- tot_ce + data1[i,4]
    i <- i + 1
  }

  i=1
  while (i < fim) {
    tot_jo <- tot_jo + data1[i,5]
    i <- i + 1
  }

  i=1
  while (i < fim) {
    tot_br <- tot_br + data1[i,6]
    i <- i + 1
  }

  j <- j + 1
}
tot <- c(tot_ar,tot_bo, tot_br, tot_ce, tot_jo)
pct <- round(tot/sum(tot)*100)
lbls <- paste(names, " ", pct, "%",sep = "")
pie(tot, labels = lbls, col = c("blue", "red", "purple", "yellow", "orange"), main = "Pesquisa do dia 14 entre 15h20 às 23h40")
barplot(tot, legend = names, col = cores, main = "Pesquisa do dia 14 entre 15h20 às 23h40", xlab = "Candidatos", ylab = "Vezes que foi pesquisado")


data1 = read.csv("Allan/Dados/p_sp_Todos_0.csv", TRUE)
data2 = read.csv("Allan/Dados/p_sp_Todos_1.csv", TRUE)
data3 = read.csv("Allan/Dados/p_sp_Todos_2.csv", TRUE)

i=1
while (i < 181) {
  if (data1[i,6] == data2[i,5] && data1[i,6] == data3[i,5]){
    print("")
  } else {
    print(data1[i,0], data1[i,6], data2[i,0], data2[i,5], data3[i,0],  data3[i,5])
  }
  i <- i + 1
}


fim = 181
i=1
while (i < fim) {
  tot_mf <- tot_mf + data2[i,2]
  i <- i + 1
}

i=1
while (i < fim) {
  tot_mh <- tot_mh + data2[i,3]
  i <- i + 1
}

i=1
while (i < fim) {
  tot_or <- tot_ce + data2[i,4]
  i <- i + 1
}

i=1
while (i < fim) {
  tot_lf <- tot_lf + data2[i,6]
  i <- i + 1
}

i=1
while (i < fim) {
  tot_an <- tot_an + data3[i,2]
  i <- i + 1
}

i=1
while (i < fim) {
  tot_ac <- tot_ac + data3[i,3]
  i <- i + 1
}

i=1
while (i < fim) {
  tot_jt <- tot_jt + data3[i,4]
  i <- i + 1
}
names <- c( "PSDB - Bruno Covas","PATRI - Arthur do Val", "PSOL - Guilherme Boulos",                   "Outros", "REPUB - Celso Russomano","PSD - Andrea Mattarazo","PCDOB - Orlando Silva", "PSB - Márcio França", "PSL - Joice H.")
cores = c(       "purple",         "blue",              "red",                     "gray",          "yellow",           "green",        "black",        "orange",             "pink")
tot    <- c(       tot_br,         tot_ar,             tot_bo,tot_mh+tot_lf+tot_ac+tot_jt,            tot_ce,            tot_an,         tot_or,          tot_mf,             tot_jo)
pct <- round(tot/sum(tot)*100)
lbls <- paste(names, " ", pct, "%",sep = "")
pie(tot, labels = lbls, xlab = "Google Trend",  col = cores, main = "Pesquisas entre nos dias 14 e 15(15h - 15h)")
barplot(tot, legend = names, col = cores, main = "Pesquisas entre nos dias 14 e 15(15h - 15h)", xlab = "Candidatos", ylab = "Vezes que foi pesquisado")

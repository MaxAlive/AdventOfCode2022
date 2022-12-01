mydata <- scan(file = "./Day01/input.txt", blank.lines.skip = FALSE)

current_sum <- 0
sums_vector <- c()

for (element in mydata) {
    if (!is.na(element)) {
        current_sum <- current_sum + element
    } else {
        sums_vector <- append(sums_vector, current_sum)
        current_sum <- 0
    }
}

print(max(sums_vector))

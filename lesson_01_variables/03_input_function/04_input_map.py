score_1, score_2, score_3, score_4, score_5 = map(int, input("Enter 5 scores: ").split())

# 1.  "Enter 5 scores: "  -> one long string "12 15 16 18 10"
# 2.  split() -> "12" | "15" | "16" | "18" | "10"
# 3.  int -> "12" | "15" | "16" | "18" | "10" -> 12 15 16 18 10
# 4. score_1, score_2, score_3, score_4, score_5 <- 12 15 16 18 10


print(score_2 + score_1 + score_3 + score_4 + score_5)


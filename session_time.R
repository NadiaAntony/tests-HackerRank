library(tidyverse)
#' Given a list of session logs, return the IDs that have (signout timestamp - signin timestamp ) >= maxspan
#' 
#' @param logs input format: 'ID timestamp sign-out/sign-in'
#' @return vector of IDs.
#' @examples

get_validsession <- function(logs) {
    data <- logs %>%
        spread(key = action, value = timestamp) %>%
        mutate(sessiontime = `sign-out` - `sign-in`) %>%
        mutate(validID = ifelse(sessiontime >= maxspan, TRUE, FALSE))
    
    result <- sort(data$ID[data$validID])
    return(result)
}

## example data
writeLines("30 99 sign-in
30 105 sign-out
12 100 sign-in
20 80 sign-in
20 120 sign-out
21 110 sign-in", "test.txt" )
logs <- read.delim("test.txt", sep=" ")
names(logs) <- c('ID', 'timestamp', 'action')

maxspan <- 20

get_validsession(logs)

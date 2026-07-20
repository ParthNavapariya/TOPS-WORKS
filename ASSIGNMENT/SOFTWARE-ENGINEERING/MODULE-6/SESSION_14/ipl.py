# Build a dynamic nested dictionary to store IPL cricket match scores: for each team, store a dictionary of player names and their runs. Add at least two teams with three players each, then print the runs scored by a specific player of your choice.

ipl_score = {
    "team1":{
        "virat":110,
        "dhoni":220,
        "gil":230
    },
    "team2":{
        "hardik":110,
        "sachin":220,
        "sauray":230
    }
}
print(ipl_score["team1"])

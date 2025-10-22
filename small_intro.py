print("Rise and Shine")

x = [1, 2, 3]
y = [1, 3, 4]

# this iterates using list comprehension
[number + 2 for number in x]

# if i want to add all elements together
[number1 + number2 for number1, number2 in zip(x, y)]

for number1, number2 in zip(x, y):
    print(number1 + number2)

## install packages (in terminal)
## create environment
# pip install palmerpenguins polars plotnine pyarrow

## import
from palmerpenguins import load_penguins
import polars as pl  # data manipulation

penguins = load_penguins(drop_na=True)

penguins = pl.from_pandas(penguins)

# this works
penguins.filter(
    pl.col("bill_length_mm") > 40,
    pl.col("bill_length_mm") <= 50,
)

# but this is preferred
penguins.filter(
    pl.col("bill_length_mm").gt(40),
    pl.col("bill_length_mm").le(50),
).with_columns(  # mutate kind of function
    new_col=pl.col("bill_length_mm") / pl.col("bill_depth_mm")
).group_by(
    "species"
).agg(  ## summarise kind of function
    pl.col("bill_length_mm").mean()
)

penguins.group_by("species").len()

from plotnine import *  ## * means everything

## using plotnine is like ggplot code
plot = (
    ggplot(
        penguins,
        aes(x="flipper_length_mm", y="body_mass_g", color="species"),
    )
    + geom_point()
    + labs(
        title="Palmer Penguins: flipper length vs body mass",
        x="Flipper length (mm)",
        y="boddy mass (g)",
        color="Species",
    )
    + theme_minimal()
)
print(plot)

plot.save("my_file.png")

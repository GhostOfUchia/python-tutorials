"""
What Are Options in Pandas?

Pandas has a built-in system for configuring settings that affect:

Display (how results look)

Performance (how fast it runs)

Precision (how many decimals you see)

Warnings, etc.

You can change these settings using:

👉 pd.set_option()

Set or modify a pandas option.

👉 pd.get_option()

Check the current value of an option.

👉 pd.reset_option()

Reset a specific option to its default.
"""
# Common Options and Their Uses
# 1️⃣ Display Options
# ✅ Show more rows or columns
import pandas as pd

pd.set_option('display.max_rows', 100)   # Default: 10
pd.set_option('display.max_columns', 20) # Default: 20

print(pd.get_option('display.max_rows'))  # Check current setting
print(pd.get_option('display.max_columns'))  # Check current setting

# ✅ Control column width
pd.set_option('display.max_colwidth', 50)

# ✅ Control float precision
pd.set_option('display.precision', 3)


# This controls how many decimal places are shown (not how many are stored).

# 2️⃣ Performance Options
# ✅ Control the number of rows read from large CSV files (for preview)
pd.options.display.max_rows = 60

# ✅ Optimize chained assignment warnings
pd.set_option('mode.chained_assignment', None)  # Hides SettingWithCopyWarning


# ⚠️ Be careful — this hides warnings that might be important for debugging.

# 3️⃣ Reset to Defaults
pd.reset_option('display.max_rows')


# Or reset all options:

pd.reset_option('all')

# 🔹 Example in Action
import pandas as pd

data = {'A': range(1, 101), 'B': range(101, 201)}
df = pd.DataFrame(data)

# Show only first 10 rows by default
print(df)

# Change option to show more
pd.set_option('display.max_rows', 100)
print(df)  # Now shows all 100 rows
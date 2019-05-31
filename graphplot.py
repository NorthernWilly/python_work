import matplotlib.pyplot as plt


Year=[2010,2011,2012,2013,2014,2015]
Rice=[1100,1300,1200,1600,1300,1400]

plt.xlabel("Years")
plt.ylabel("Rice Production")
plt.title("Rice Production by Year")
plt.plot(Year,Rice)
plt.show()

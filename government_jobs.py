"""
    The weighted round
    input: list of party with their mandates and their preferences
    output: for any party list of the jobs the are got

    algo:
    1. while have more bags calculate for any party thier mandates / f(s)=s+y+1
    2. the party with the large dose choose their choices.
 """
import random

# party class
class party:

    def __init__(self, name, mandets, preferences):
        self.name = name  # party name
        self.mandets = mandets  # number of mandets the party got
        self.preferences = preferences  # dict of preferences for the jobs (office,val)
        self.jobs = set()  # set of the jobs the are got
        self.right = 0  # max right


# Division of portfolios
def loot_distribution(y:float, gover_office:set, coalition: list):

    while len(gover_office) > 0:
        # calculate the party right
        for p in coalition:
            p.right = p.mandets / (len(p.jobs) + y+1)

        # find the party with the larges right
        p=coalition[0]
        for pr in coalition:
            if p.right<pr.right:
                p=pr

        #choose for this party the office the wants
        office=gover_office[0]

        for o in gover_office:
            if(p.preferences[office]<p.preferences[o]):
                office=o
        p.jobs.add(office)
        gover_office.remove(office)


if __name__ == '__main__':
    gover_office=["Prime Minister office", "The Deputy Prime Minister office", "Ministry of Settlement",
                 "Ministry of Interior", "Ministry of religious services", "Ministry of Construction and Housing",
                 "Ministry of Education", "Ministry of Communication", "Ministry of laws", "Jerusalem Office and Heritage",
                 "Ministry of Energy", "Ministry of Foreign Affairs", "Ministry of Economy and Industry", "Ministry of Intelligence",
                 "Ministry of Welfare and Social Security", "Ministry of Social Equality", "Ministry of Tourism", "Ministry of Defence",
                 "Ministry of Innovation, Science and Technology", "Ministry of Immigration and Integration", "Ministry of Culture and Sports",
                 "Ministry of Internal Security", "Ministry of Transportation", "Ministry of Diaspora", "Ministry of Finance",
                 "Ministry of Agriculture and Rural Development", "Ministry of Peripheral, Negev and Galilee Development",
                 "Ministry of Health", "Ministry of Environmental Protection", "Ministry of Regional Cooperation"
                 ]
    number_of_colation = int(input("enter number of party in collation\n"))
    colation_list=[]
    for i in range(number_of_colation):

        party_name=input("enter party name\n")
        party_mandets=int(input("enter mandets total\n"))
        party_preferences=dict()
        for office in gover_office:
            val_right=random.randint(1, 10)
            party_preferences[office]=val_right
        new_party=party(party_name, party_mandets, party_preferences)
        colation_list.insert(-1, new_party)
    y=int(input("enter y val\n"))
    loot_distribution(y, gover_office, colation_list)
    for z in colation_list:
        print(z.name+" office:"+str(z.jobs)+"\n")


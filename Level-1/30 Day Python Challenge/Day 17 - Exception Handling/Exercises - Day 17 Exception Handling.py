# names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

nordic_countries = names[:5]
es, ru = names[-2:]

print("Nordic Countries:", nordic_countries)
print("Estonia:", es)
print("Russia:", ru)
Universities = {
  "ID" : 1,
  "Name" : "University of the Philippines",
  "Location" : "Quezon",
  "Established Year" : 1908 ,
  "Type" : "Public",
  "Website" : "www.up.edu.ph"
},{
  "ID" : 2,
  "Name" : "Ateneo de Manila University",
  "Location" : "Quezon",
  "Established Year" : 1859,
  "Type" : "Private",
  "Website" : "www.ateneo.edu"
},{
  "ID" : 3,
  "Name" : "De La Salle University",
  "Location" : "Manila",
  "Established Year" : 1911,
  "Type" : "Private",
  "Website" : "www.dlsu.edu.ph"
},{
  "ID" : 4,
  "Name" : "University of Santo Tomas",
  "Location" : "Manila",
  "Established Year" : 1611,
  "Type" : "Private",
  "Website" : "www.ust.edu.ph"
},{
  "ID" : 5,
  "Name" : "Polytechnic University of the Philippines",
  "Location" : "Manila",
  "Established Year" : 1904,
  "Type" : "Public",
  "Website" : "www.pup.edu.ph"
}
for University in Universities:
    print(f"ID: {University['ID']}, Name: {University['Name']}, Location: {University['Location']}, Established Year: {University['Established Year']}, Type: {University['Type']}, Website: {University['Website']}")
Restaurants = {
  "ID" : 1,
  "Name" : "Vikings Luxury Buffet",
  "Location" : "Pasay City",
  "Cuisine Type" : "Buffet",
  "Established Year" : 2011,
  "Website" : ""
},{
  "ID" : 2,
  "Name" : "Antonio\'s Restaurant",
  "Location" : "Tagaytay",
  "Cuisine Type" : "Fine Dining",
  "Established Year" : 2002,
  "Website" : "www.antoniosrestaurant.ph"
},{
  "ID" : 3,
  "Name" : "Mesa Filipino Moderne",
  "Location" : "Makati City",
  "Cuisine Type" : "Filipino",
  "Established Year" : 2009,
  "Website" : "www.mesa.ph"
},{
  "ID" : 4,
  "Name" : "Manam Comfort Filipino",
  "Location" : "Quezon City",
  "Cuisine Type" : "Filipino",
  "Established Year" : 2013,
  "Website" : "www.manam.ph"
},{
  "ID" : 5,
  "Name" : "Ramen Nagi",
  "Location" : "Various Locations",
  "Cuisine Type" : "Japanese",
  "Established Year" : 2013,
  "Website" : "www.ramennagi.com.ph"
}
for Restaurant in Restaurants:
    print(f"ID: {Restaurant['ID']}, Name: {Restaurant['Name']}, Location: {Restaurant['Location']}, Cuisine Type: {Restaurant['Cuisine Type']}, Established Year: {Restaurant['Established Year']}, Website: {Restaurant['Website']}")
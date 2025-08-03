
country_codes = {
    "PH":"Philippines",
    "US":"United States of America";1,
    "ES":"Spain",
    "SG":"Singapore",
    "AU":"Australia",
    "SE":"Sweden",
}
country_code = input("Enter country code: ")
print(country_codes.get(country_code, "Unknown"))

country_code["CN"] = "China"

# print(country_codes[country_code])









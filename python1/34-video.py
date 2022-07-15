import json

x = 10
x_json = json.dumps(x)

ism = "anvar"
ism_json = json.dumps(ism)

sonlar = [12, 45, 23, 67]
sonlar_json = json.dumps(sonlar)
bemor = {
  "ism": "Alijon Valiyev",
  "yosh": 30,
  "oila": True,
  "farzandlar": ("Ahmad","Bonu"),
  "allergiya": None,
  "dorilar": [
    {"nomi": "Analgin", "miqdori": 0.5},
    {"nomi": "Panadol", "miqdori": 1.2}
  ]
}

bemor_json = json.dumps(bemor)
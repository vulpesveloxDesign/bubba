from django import forms

class ContactForm(forms.Form):
    title           = forms.CharField(label='Emne', max_length=100, required=True)
    content         = forms.CharField(label='Besked', widget=forms.Textarea, required=True)
    sender          = forms.EmailField(label='Afsender (din email)')

METHOD_TYPE = ("terra", "aqua", "coco", "COGr", "hydro, soft", "hydro, hard")
WATER_TYPE = ("blødt vand", "middelhårdt vand", "hårdt vand")
RHYTHM_TYPE = ("let kost", "mellem kost", "tung kost")
CONDUCTION_TYPE = ("PPM (truncheon)", "PPM (eutech)", "PPM (hanna)", "EC", "CF")

class NameForm(forms.Form):
    method = forms.ChoiceField(label='Metode', choices=[(x,x) for x in METHOD_TYPE])
    tank_size = forms.IntegerField(label='Tankstørrelse')
    water_type = forms.ChoiceField(label='Vandtype', choices=[(x,x) for x in WATER_TYPE])
    water_hardness = forms.IntegerField(label='Hårdhed')
    rhythm = forms.ChoiceField(label='Rytme', choices=[(x,x) for x in RHYTHM_TYPE])
    conductivity = forms.ChoiceField(label='Ledeevne', choices=[(x,x) for x in CONDUCTION_TYPE])

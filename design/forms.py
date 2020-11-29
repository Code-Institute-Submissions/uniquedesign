from django import forms
from .models import Product, Category, Header, Quantity, Edge, Cardtype, Thicknes, Papermake, Papertype


class DesignForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'category', 'quantity', 'edge',
                  'cardtype', 'thicknes', 'paper',
                  'make', 'header', 'logo', 'info', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        quantity = Quantity.objects.all()
        edge = Edge.objects.all()
        header = Header.objects.all()
        cardtype = Cardtype.objects.all()
        thicknes = Thicknes.objects.all()
        paper = Papertype.objects.all()
        make = Papermake.objects.all()

        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        q_friendly_names = [(q.id, q.get_friendly_name()) for q in quantity]
        e_friendly_names = [(e.id, e.get_friendly_name()) for e in edge]
        h_friendly_names = [(h.id, h.get_friendly_name()) for h in header]
        ct_friendly_names = [(ct.id, ct.get_friendly_name()) for ct in cardtype]
        t_friendly_names = [(t.id, t.get_friendly_name()) for t in thicknes]
        pt_friendly_names = [(pt.id, pt.get_friendly_name()) for pt in paper]
        pm_friendly_names = [(pm.id, pm.get_friendly_name()) for pm in make]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        self.fields['quantity'].choices = q_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        self.fields['edge'].choices = e_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        self.fields['header'].choices = h_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        self.fields['cardtype'].choices = ct_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        self.fields['thicknes'].choices = t_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        self.fields['paper'].choices = pt_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        self.fields['make'].choices = pm_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

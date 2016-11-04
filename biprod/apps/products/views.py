from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from biprod.apps.products.models import Products
from django.http import HttpResponseRedirect, HttpResponse
from biprod.apps.products.forms import ProductsForm

class ProductsCreateView(CreateView):
    form_class = ProductsForm
    template_name= 'apps/products/products.html'
    model = Products
    
    def form_valid(self, form):
        print ("HOLA: "),form
        form.instance.created_by = self.request.user
        return super(ProductsCreateView, self).form_valid(form)
        
    #def post(self, request, *args, **kwargs):
        """nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        stock = request.POST.get('stock')
        precio = request.POST.get('precio')
        #print ("DATA",stock)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            new_reg = form.save(commit=False)
            new_reg.save()
        
        return HttpResponse('exito')"""
    def post(self, request, *args, **kwargs):
        """if request.method == 'POST':
            form = ProductsForm(request.POST, request.FILES)
            if form.is_valid():
                newdoc = ProductsForm(foto = request.FILES['foto'])
                newdoc.save()
                return HttpResponse('exito')"""
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            stock = form.cleaned_data['stock']
            precio = form.cleaned_data['precio']
            foto   = form.cleaned_data['foto']
            p = Products()
            p.nombre = nombre
            p.descripcion = descripcion
            p.stock = stock
            p.precio = precio
            p.foto = foto
            p.save()
            return HttpResponse('exito')
        

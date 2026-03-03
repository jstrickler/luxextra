"""
    Views for the Django Forms Demo
"""
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render, redirect    
# from .forms import DemoForm, ArtistDeleteForm
# from .forms import ArtistDeleteDropdownForm, ArtistForm
from artworks.models import Artist, Artwork

class HomeView(TemplateView):
    """
    HomeView landing page for basic forms demo
    """
    template = "formsdemo/home.html"

#TODO:   NEEDS A LOT OF WORK!!

class ArtworkSearchView():
    model = Artwork

def artworkdetails(request, pk):
    """Show details for one hero"""
    hero = get_object_or_404(Superhero, pk=pk)
    data = {'hero': hero, 'added': ''}
    return render(request, 'formsdemo/hero_details.html', data)


def heroadded(request, pk):
    """Display details for newly added hero"""
    hero = get_object_or_404(Superhero, pk=pk)
    data = {'hero': hero, 'added': 'Added:'}
    return render(request, 'formsdemo/hero_details.html', data)


def heroadd(request, layout_type):
    """
        Add a new hero to the database
    
        Different templates will be used based on the URL, 
        but the same form for all.
    """
    add_template = f"formsdemo/hero_add_{layout_type}.html"
    if request.method == 'POST':
        # bound (filled-in) form
        form = HeroModelForm(request.POST)
        if form.is_valid():
            form.save()  # write data to DB
            hero_name = form.cleaned_data['name']
            return redirect(
                'formsdemo:heroadded',
                hero_name=hero_name,
            )
    else:
        # unbound (empty) form
        form = HeroModelForm()

    context = {
        'page_title': 'Add Hero',
        'form': form,
    }
    return render(request, add_template, context)


def herodelete(request):
    """
    Delete a hero by name

    Goes to hero list on successful deletion
    """

    # bound (filled-in) form
    if request.method == 'POST':
        form = HeroDeleteForm(request.POST)
        if form.is_valid():
            hero_name = form.cleaned_data['hero_name']
            hero = get_object_or_404(Superhero, name=hero_name)
            hero.delete()
            return redirect('formsdemo:herolist')
    else:
        # unbound (empty) form
        form = HeroDeleteForm()

        context = {
            'page_title': 'Delete Hero',
            'form': form,
        }
        return render(request, 'formsdemo/hero_delete.html', context)

def herodeletedropdown(request):
    """
    Delete a hero by name from a dropdown list

    Goes to hero list on successful deletion
    """

    # bound (filled-in) form
    if request.method == 'POST':
        form = HeroDeleteDropdownForm(request.POST)
        if form.is_valid():
            hero_name = form.cleaned_data['hero']
            hero_obj = get_object_or_404(Superhero, name=hero_name)
            hero_obj.delete()
            return redirect('formsdemo:herolist')
    else:
        # unbound (empty) form
        form = HeroDeleteDropdownForm()

    context = {
        'page_title': 'Delete Hero',
        'form': form,
    }
    return render(request, 'formsdemo/hero_delete_dropdown.html', context)



def demo(request):
    """
    Form field demo
    """
    invalid = False

    if request.method == 'POST':  # if form is bound (i.e., filled in)
        form = DemoForm(request.POST)
        if form.is_valid():
            # if data is valid, show results page
            context = {
                    'page_title': 'Form Fields Results',
                    'data': form.cleaned_data,
            }
            return render(request, 'formsdemo/demo_results.html', context)
        else:
            # show form with errors for correcting
            invalid = True
    else:
        form = DemoForm()  # unbound (not filled in) form

    # unless POST/valid, redraw form
    context = {
        'page_title': 'Form Fields Example',
        'form': form,
        'invalid': invalid,
    }
    return render(request, 'formsdemo/demo.html', context)

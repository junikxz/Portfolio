# main/models.py

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200, help_text="Pisahkan setiap teknologi dengan koma, contoh: Python, Django, HTML")
    
    # URLField yang opsional
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True) # DITAMBAHKAN

    def __str__(self):
        return self.title

    # DITAMBAHKAN: Fungsi penting untuk memperbaiki error di template
    def get_tech_stack_as_list(self):
        """
        Mengambil string dari field 'tech_stack' dan mengubahnya 
        menjadi sebuah list yang bisa digunakan di template.
        """
        if self.tech_stack:
            return [tech.strip() for tech in self.tech_stack.split(',')]
        return []
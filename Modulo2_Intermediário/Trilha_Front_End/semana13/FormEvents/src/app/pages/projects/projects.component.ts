import { NgFor, NgIf } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { Observable } from 'rxjs';

interface IgitHubRespose{
  projectName: string,
  projectLink: string
}
@Component({
  selector: 'app-projects',
  standalone: true,
  imports: [NgFor,NgIf],
  templateUrl: './projects.component.html',
  styleUrl: './projects.component.css'
})

export class ProjectsComponent {
  projetos:IgitHubRespose[]| null = []
  
  constructor(private http: HttpClient) { 
    
  }

  getProjects(): Observable<any>{
    return this.http.get('https://api.github.com/users/ManoelPatrocinio/repos')
  }

  ngOnInit(): void {
    this.getProjects().subscribe((response) => {
      response.map((item:any)=>{

       
        this.projetos?.push({
          projectName : item.name,
          projectLink: item.html_url
        })


       
      })
    })

  }
}

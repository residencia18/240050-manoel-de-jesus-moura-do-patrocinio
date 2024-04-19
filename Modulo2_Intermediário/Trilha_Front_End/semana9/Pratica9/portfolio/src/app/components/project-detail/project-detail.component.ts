import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component } from '@angular/core';
import { ProjectType } from '../../types/project';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-project-detail',
  standalone: true,
  imports: [HttpClientModule],
  templateUrl: './project-detail.component.html',
  styleUrl: './project-detail.component.css'
})
export class ProjectDetailComponent {
  project: ProjectType|null
  projectId: string
  urlToJson = '../assets/projects.json';

  
  constructor(public http: HttpClient,private rota: ActivatedRoute) {
    this.project = null;
    this.projectId = ""
  }
  ngOnInit(): void{
    this.projectId = this.rota.snapshot.params['id']
    this.http.get<ProjectType[]>(this.urlToJson).subscribe(response => {
      this.project = response.filter((proj) =>  proj.id == this.projectId)[0];
    });
  }

}

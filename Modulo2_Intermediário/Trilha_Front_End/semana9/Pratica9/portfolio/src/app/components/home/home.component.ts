import { Component } from '@angular/core';
import { ProjectType } from '../../types/project';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { NgFor } from '@angular/common';
import { CardProjectComponent } from '../card-project/card-project.component';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [HttpClientModule,NgFor, CardProjectComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  urlToJson = '../assets/projects.json';
  projectsList: ProjectType[] | []

  constructor(public http: HttpClient) {
    this.projectsList = []
  }

  ngOnInit(): void {
    this.http.get<any>(this.urlToJson).subscribe(response => {
      this.projectsList = response;
      console.log("projets", this.projectsList)
    });
  }
}

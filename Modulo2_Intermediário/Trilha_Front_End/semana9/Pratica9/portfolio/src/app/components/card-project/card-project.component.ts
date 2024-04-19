import { Component, Input } from '@angular/core';
import { ProjectType } from '../../types/project';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-card-project',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './card-project.component.html',
  styleUrl: './card-project.component.css'
})
export class CardProjectComponent {
  @Input() project:ProjectType | null 
  
  constructor() {
    this.project = null;
  }
}

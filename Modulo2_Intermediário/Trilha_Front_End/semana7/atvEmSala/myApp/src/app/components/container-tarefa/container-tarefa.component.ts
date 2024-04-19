import { NgFor } from '@angular/common';
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-container-tarefa',
  standalone: true,
  imports: [NgFor],
  templateUrl: './container-tarefa.component.html',
  styleUrl: './container-tarefa.component.css'
})
export class ContainerTarefaComponent {
  @Input() todos:string[] = [];
}

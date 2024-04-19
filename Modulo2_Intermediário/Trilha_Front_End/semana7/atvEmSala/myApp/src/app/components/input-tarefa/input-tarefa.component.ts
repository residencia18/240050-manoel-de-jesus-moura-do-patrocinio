import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-input-tarefa',
  standalone: true,
  imports: [],
  templateUrl: './input-tarefa.component.html',
  styleUrl: './input-tarefa.component.css'
})
export class InputTarefaComponent {

  @Output() tarefaAdicionada = new EventEmitter<string>();

  addEventTarefa(item: string) {
    this.tarefaAdicionada.emit(item);
  }
}


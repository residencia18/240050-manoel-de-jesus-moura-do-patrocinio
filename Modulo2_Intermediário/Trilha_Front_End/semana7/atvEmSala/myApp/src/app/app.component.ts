import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { InputTarefaComponent } from './components/input-tarefa/input-tarefa.component';
import { ContainerTarefaComponent } from './components/container-tarefa/container-tarefa.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, InputTarefaComponent,ContainerTarefaComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'myApp';
  todoList:string[] = ["acordar","cafe"];

  addTodoOnArray(item:any) {
    this.todoList.push(item)
  }
}

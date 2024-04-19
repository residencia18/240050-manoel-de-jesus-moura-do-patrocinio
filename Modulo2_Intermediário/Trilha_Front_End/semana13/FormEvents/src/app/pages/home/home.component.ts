import { Component } from '@angular/core';
import { FormEventsService } from '../../services/form-events.service';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  public title = 'Home';

  constructor( private formService : FormEventsService){
    this.formService.getFormData().subscribe(
      (data)=>{
        console.log('Dados do formulário', data)
      },
      error => {
        console.log('Erro ao receber os dados do formulário:', error);
      } 
    ),
    this.formService.getFormEvent().subscribe(
      (data)=>{
        console.log('Eventos do Formulário', data)
      },
      error => {
        console.log('Erro ao receber os dados dos eventos:', error);
      } 
    )
  }



}

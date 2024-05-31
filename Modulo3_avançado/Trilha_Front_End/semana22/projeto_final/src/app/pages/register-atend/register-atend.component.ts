import { Component } from '@angular/core';
import { FormAtendimentoComponent } from '../../components/form-atendimento/form-atendimento.component';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-register-atend',
  standalone: true,
  imports: [FormAtendimentoComponent],
  templateUrl: './register-atend.component.html',
  styleUrl: './register-atend.component.css'
})
export class RegisterAtendComponent {

}

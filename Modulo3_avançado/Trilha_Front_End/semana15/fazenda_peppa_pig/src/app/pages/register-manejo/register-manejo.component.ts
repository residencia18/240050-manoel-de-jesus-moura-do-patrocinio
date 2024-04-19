import { Component } from '@angular/core';
import { FilterSuinosManejoComponent } from '../../components/filter-suinos-manejo/filter-suinos-manejo.component';
import { FilterSuinosComponent } from '../../components/filter-suinos/filter-suinos.component';
import { type_suino } from '../../types/type_suino';
import { ApiService } from '../../services/api.service';
import { CardSuinoDetailComponent } from '../../components/card-suino-detail/card-suino-detail.component';
import { NgFor, NgIf } from '@angular/common';
import { Subscription } from 'rxjs';
import { DateInMonthsPipe } from "../../pipes/date-in-months.pipe"
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';


interface animalAtividade {
  suinoBrinco: string,
  atividades: {
    atv_name: "Raiva" | "Rinite_Atrófica" | "Parvovirose_Suína"
    atv_status: boolean
  }
}
@Component({
  selector: 'app-register-manejo',
  standalone: true,
  imports: [FilterSuinosManejoComponent, FilterSuinosComponent, CardSuinoDetailComponent, NgFor, NgIf, DateInMonthsPipe, ReactiveFormsModule],
  templateUrl: './register-manejo.component.html',
  styleUrl: './register-manejo.component.css'
})
export class RegisterManejoComponent {
  listSuinos: type_suino[] = [];
  filteredListSuinos: type_suino[] = [];
  listSuinosSelectedToManejo: type_suino[] = [];
  optionSelected: any = { propriedade: null, valor: null };
  private subscription: Subscription | null = null;
  registerStep: boolean = false
  registerSectionForm: FormGroup = new FormGroup({});
  listAnimaisAtividade: animalAtividade[] = []




  constructor(private apiService: ApiService, private formBuilder: FormBuilder, private rotas: Router) { }

  ngOnInit(): void {
    this.subscription = this.apiService.getListaSuinos().subscribe(
      (datas: type_suino[]) => {
        this.listSuinos = datas;
        this.filteredListSuinos = this.listSuinos;
      },
      error => {
        // Lide com o erro de forma adequada, como exibindo uma mensagem de erro.
        console.error('Erro ao obter lista de suínos:', error);
      }
    );

    this.registerSectionForm = this.formBuilder.group({
      's_date': [null, [Validators.required]],
      's_description': [null, [Validators.required]],
      's_brincoAnimal': [null, [Validators.required]],
      's_atividades': [null, [Validators.required]],

    })
  }

  filterList(filter: { propriedade: keyof type_suino, valor: string }): void {
    this.filteredListSuinos = this.listSuinos.filter(suino => suino[filter.propriedade] == filter.valor);
  }

  clearFilter(): void {
    this.filteredListSuinos = this.listSuinos;
  }

  addSuinoToManejoList(suinoSelected: type_suino): void {
    if (!this.listSuinosSelectedToManejo) {
      this.listSuinosSelectedToManejo = []; // Inicialize a lista se ainda não estiver definida

    }

    if (suinoSelected && !this.listSuinosSelectedToManejo.includes(suinoSelected)) {
      this.listSuinosSelectedToManejo.push(suinoSelected);
    }
  }
  removeSuinoToManejoList(suinoSelected: type_suino): void {
    if (suinoSelected && this.listSuinosSelectedToManejo.includes(suinoSelected)) {
      this.listSuinosSelectedToManejo = this.listSuinosSelectedToManejo.filter((value) => value !== suinoSelected);
    }
  }

  toggleStep() {
    this.registerStep = !this.registerStep;
  }

  setAnimalAndAtividades() {

    if (this.listAnimaisAtividade.some(atv => atv.suinoBrinco === this.registerSectionForm.get("s_brincoAnimal")?.value)) {
      Swal.fire({
        title: 'Error !',
        icon: 'error',
        text: 'Oppss... esse animal já foi adicionado na sessão.',
        showConfirmButton: true,

      })
    } else {
      let newItem = {
        suinoBrinco: this.registerSectionForm.get("s_brincoAnimal")?.value,
        atividades: this.registerSectionForm.get("s_atividades")?.value.map((atv: any) => {
          return { atv_name: atv, atv_status: false }
        })
      }
      this.listAnimaisAtividade.push(newItem);
      this.registerSectionForm.get("s_brincoAnimal")?.reset()
      this.registerSectionForm.get("s_atividades")?.reset()
      console.log("this.listAnimaisAtividade", this.listAnimaisAtividade)

    }

  }

  onSubmit(form: FormGroup) {
    const sessao = {
      s_date: form.value.s_date,
      s_description: form.value.s_description,
      s_animais: this.listAnimaisAtividade,
    }
    this.apiService.cadastroSessao(sessao).subscribe((data) => {
      Swal.fire({
        title: 'Sucesso !',
        icon: 'success',
        showConfirmButton: false,
        timer: 1500
      })
      setTimeout(() => {
        window.location.reload();
      }, 1700)
    });
  }
  ngOnDestroy(): void {
    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }
}

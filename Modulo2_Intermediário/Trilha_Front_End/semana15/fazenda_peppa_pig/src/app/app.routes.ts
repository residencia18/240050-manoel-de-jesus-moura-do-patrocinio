import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { CadastroSuinosComponent } from './pages/cadastro-suinos/cadastro-suinos.component';
import { ListagemSuinosComponent } from './pages/listagem-suinos/listagem-suinos.component';
import { LoginComponent } from './pages/login/login.component';
import { CadastroUsuarioComponent } from './pages/cadastro-usuario/cadastro-usuario.component';
import { EdicaoSuinoComponent } from './pages/edicao-suino/edicao-suino.component';
import { RegisterPesoComponent } from './pages/register-peso/register-peso.component';
import { EditPesoComponent } from './pages/edit-peso/edit-peso.component';
import { AuthGuard,canActivateGuard } from './auth-guard.guard';
import { RegisterManejoComponent } from './pages/register-manejo/register-manejo.component';
import { ListManejoComponent } from './pages/list-manejo/list-manejo.component';
import { ManegerManejoComponent } from './pages/maneger-manejo/maneger-manejo.component';

/* foi apresentado o  error que não conseguir resolver ao usar o Guar canActivate:
    ERROR NullInjectorError: R3InjectorError(Environment Injector)[_AuthGuard -> _AuthService -> _HttpClient -> _HttpClient]: 
    NullInjectorError: No provider for _HttpClient!

    As possíveis soluções que encontrei não funcionam com o projeto em Angular 17, com standalone:true sem o arquivo app.module.ts.
    E não tive tempo, nem era viável  alterar a estrutura do projeto já no final.

*/


export const routes: Routes = [
    {path:"", component: HomeComponent},
    {path:"register-suino",  component: CadastroSuinosComponent},
    {path:"list-suino", component: ListagemSuinosComponent},
    {path:"edit-suino/:id", component: EdicaoSuinoComponent},

    {path:"register-peso/:id", component: RegisterPesoComponent},
    {path:"edit-peso/:id", component: EditPesoComponent},

    {path:"login", component: LoginComponent},
    {path:"register", component: CadastroUsuarioComponent},

    {path:"register-manejo", component: RegisterManejoComponent},
    {path:"list-manejo", component: ListManejoComponent},
    {path:"menage-manejo", component: ManegerManejoComponent},

];

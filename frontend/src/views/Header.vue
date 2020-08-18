<template>
    <div>
        <b-navbar id="navbar" toggleable="lg" type="light" variant="warning">
            <div class="container">
            <b-navbar-brand href="#" id="branding">Mapishi</b-navbar-brand>

            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav>
                 <b-nav-item>
                    <b-link to="/" router-tag='li' exact>Home</b-link>
                </b-nav-item>

                <b-nav-item>
                    <b-link to="/add-recipe" router-tag='li' exact>Add recipe</b-link>
                </b-nav-item>

                <b-nav-item href="#" disabled>Disabled</b-nav-item>
            </b-navbar-nav>

            <!-- Right aligned nav items -->
            <b-navbar-nav class="ml-auto" align='center'>
                <b-nav-form>
                <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
                <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
                </b-nav-form>

                <b-nav-item-dropdown right>
                <!-- Using 'button-content' slot -->
                <template v-slot:button-content>
                    <em>User</em>
                </template>
                <b-dropdown-item href="#">Profile</b-dropdown-item>
                <b-dropdown-item href="#">Sign Out</b-dropdown-item>
                </b-nav-item-dropdown>
            </b-navbar-nav>
            </b-collapse>
         </div>
        </b-navbar>
    </div>
</template>

<style scoped>
    #navbar {
        /* border-radius: 1rem; */
        box-shadow: 0 2px 10px rgba(0,0,0, .3);
    }

    #navbar a {
        font-weight: bold;
    }

    #branding {
        letter-spacing: 2px;
        text-shadow: 0 2px 10px rgba(0,0,0, .3);
        text-transform: uppercase;
    }
</style>
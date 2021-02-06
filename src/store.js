import { reactive } from "vue";

export const store = {
    state: reactive({
        activePositions: {
            fromPosition: null,
            expectedPosition: null,
            actualPosition: null
        },
        activeCard: {
            name: null,
            link: null,
            grip: null,
            category: null,
            fromPosition: null,
            expectedPosition: null,
            actualPosition: null
        },
        modalOpen: false
    }),
    changeActivePositions(newPositions) {
        this.state.activePositions.fromPosition = newPositions.fromPosition;
        this.state.activePositions.expectedPosition = newPositions.expectedPosition;
        this.state.activePositions.actualPosition = newPositions.actualPosition;
    },
    changeActiveCard(newActiveCard) {
        this.state.activeCard.name = newActiveCard.name;
        this.state.activeCard.link = newActiveCard.link;
        this.state.activeCard.grip = newActiveCard.grip;
        this.state.activeCard.category = newActiveCard.catgeory;
        this.state.activeCard.fromPosition = newActiveCard.fromPosition;
        this.state.activeCard.expectedPosition = newActiveCard.expectedPosition;
        this.state.activeCard.actualPosition = newActiveCard.actualPosition;
    },
    toggleModal() {
        this.state.modalOpen === true ? this.state.modalOpen = false : this.state.modalOpen = true;
    }
}
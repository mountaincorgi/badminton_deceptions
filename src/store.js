import { reactive } from "vue";

export const store = {
    state: reactive({
        activePositions: {
            fromPosition: null,
            expectedPosition: null,
            actualPosition: null
        }
    }),
    changeActivePositions(newPositions) {
        this.state.activePositions.fromPosition = newPositions.fromPosition;
        this.state.activePositions.expectedPosition = newPositions.expectedPosition;
        this.state.activePositions.actualPosition = newPositions.actualPosition;
    }
}